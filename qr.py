import clipboard
import subprocess

subprocess.call(['qrencode', '-o', '/tmp/qr.png', '-s', '10', clipboard.paste()])
subprocess.call(['display', '/tmp/qr.png'])
subprocess.call(['rm', '/tmp/qr.png'])
