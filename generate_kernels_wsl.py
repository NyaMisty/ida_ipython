import os

KERNEL_TEMPLATE = r'''
{{
 "display_name": "{display_name}",
 "language": "python",
 "argv": [
  "python",
  "-c",
  "{launch_script}",
  "{{connection_file}}",
  "/mnt/c/Program Files/IDA Pro 7.4/{exe_name}"
 ],
 "codemirror_mode": {{
  "version": 2,
  "name": "ipython"
 }}
}}
'''


def write_kernel(out_dir, display_name, exe_name, launch_script):
    kernel = KERNEL_TEMPLATE.format(display_name=display_name, exe_name=exe_name, launch_script=launch_script)

    kernel_dir = os.path.join(out_dir, display_name.lower())
    if not os.path.exists(kernel_dir):
        os.makedirs(kernel_dir)

    with open(os.path.join(kernel_dir, 'kernel.json'), 'wb') as f:
        f.write(kernel)


def generate_kernels(out_dir):
    with open('launch_ida_wsl.py', 'rb') as f:
        launch_ida_script = f.read()

    launch_ida_script = launch_ida_script.replace('"', r'\"').replace('\n', r'\n').replace('\r', r'\r')

    for display_name, exe_name in (('IDA32', 'ida.exe'), ('IDA64', 'ida64.exe')):
        write_kernel(out_dir=out_dir,
                     display_name=display_name,
                     exe_name=exe_name,
                     launch_script=launch_ida_script)
