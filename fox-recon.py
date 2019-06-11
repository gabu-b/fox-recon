import os,sys,datetime

#Enviroment Variables
def get_url():
    global domain
    domain = str(sys.argv[1])
    print('[i] URL choosed was: ' + domain)

def current_dir(): 
    global dirpath
    dirpath = os.getcwd() + "/"

def generate_filename(): #Return Filename
    global filename
    basename = "recon"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix]) 

#Programs
def subfinder():
    print('[i] Running subfinder on target...')
    os.system('subfinder -d ' + domain + ' -o ' + dirpath + '' + filename + ' > /dev/null 2>&1') 
    print('[i] Subfinder recon finished.')

def sublister():
    print('[i] Running sublist3r on target...')
    os.system('sublist3r -d ' + domain + ' -o ' + dirpath + '' + filename + ' > /dev/null 2>&1')
    print('[i] Sublist3r recon finished.')
    print('[i] The results are already avaliable in ' + dirpath + filename)

def main():   
    get_url()    
    current_dir()
    generate_filename()
    subfinder()
    generate_filename()
    sublister()
main()
