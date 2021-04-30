from flask import Flask
from ec2_metadata import ec2_metadata
app = Flask(__name__)

html = '<!DOCTYPE html><html><head><style>table,th,td{border:1px solid black;border-collapse:collapse;border-color:#c8c8c8;border-width:2px;padding:0.3em}</style></head><body><h2>Table With Border</h2><table><tr style="background-color: #e6e6e6;"><th>Metadata</th><th>Value</th></tr><tr><td>instance-id</td><td>'+ec2_metadata.instance_id+'</td></tr><tr><td>ami-launch-index</td><td>'+str(ec2_metadata.ami_launch_index)+'</td></tr><tr><td>public-hostname</td><td>'+ec2_metadata.public_hostname+'</td></tr><tr><td>public-ipv4</td><td>'+'none'+'</td></tr><tr><td>local-hostname</td><td>'+ec2_metadata.private_hostname+'</td></tr><tr><td>local-ipv4</td><td>'+'none'+'</td></tr></table></body></html>'


@app.route('/')
def hello_world():
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')