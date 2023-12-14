import os
#create a function to rename files

def rename_files(directory, prefix):
     for filename in os.listdir(directory):
            new_filename = prefix + ' ' + filename
            source = os.path.join(directory, filename)
            Rename = os.path.join(directory, new_filename)
        
            os.rename(source, Rename)
    
    #use the function to rename the file in the directory
rename_files(r'C:\Users\casse\Desktop\Automation\images', 'Face Recognition for')
        