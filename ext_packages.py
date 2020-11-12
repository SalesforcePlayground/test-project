import subprocess,json

def createScratchOrg():
    print('Creating so')
    createScratchOrg = subprocess.check_output(
        "sfdx force:org:create -v HubOrg -s -f config/project-scratch-def.json -a so_test --wait 10 --json",shell=True)
    createScratchOrg = json.loads(str(createScratchOrg.decode('utf-8')))
    print('Created so: ')
    print(createScratchOrg)
    return createScratchOrg

def installExtPackages():
    print('Installing ext pkgs')
    f = open('ext_packages.json',) 
    pkg_json = json.load(f) 
    print('Ext pkgs json: ')
    print(pkg_json)
    for pkg in pkg_json:
        installPackage = subprocess.check_output(
            "sfdx force:package:install --package "+pkg['package_id'] + " -u so_test -w 10 --publishwait 10 --json",shell=True)
        installPackage = json.loads(str(installPackage.decode('utf-8')))
        print("Installed package: ")
        print(installPackage)
    return True

if __name__ == '__main__':
    createScratchOrg()
    installExtPackages()
