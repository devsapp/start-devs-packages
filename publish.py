import subprocess

def getContent(fileList):
    for eveFile in fileList:
        try:
            with open(eveFile) as f:
                return f.read()
        except:
            pass
    return None

with open('update.list') as f:
    publish_list = [eve_app.strip() for eve_app in f.readlines()]

for eve_app in publish_list:
    publish_script = 'https://serverless-registry.oss-cn-hangzhou.aliyuncs.com/publish-file/python3/hub-publish.py'
    command = 'cd %s && wget %s && python hub-publish.py' % (eve_app, publish_script)
    child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,)
    stdout, stderr = child.communicate()
    if child.returncode == 0:
        print("success:", stdout)
    else:
        print("error:", stderr)
        raise ChildProcessError(stderr)
