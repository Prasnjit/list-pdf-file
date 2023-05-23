# import OS module
# import os

# Get the list of all files and directories
# path = "C://Users//ASHINI KRISHNAN//AppData//Local"
# dir_list = os.listdir(path)

# print("Files and directories in '", path, "' :")

# prints all files
# print(dir_list)


# import OS module
# import os

# # This is my path
# path = "/home/prasnjit/Downloads"
# # Scan the directory and get
# # an iterator of os.DirEntry objects
# # corresponding to entries in it
# # using os.scandir() method
# obj = os.scandir()

# # List all files and directories in the specified path
# print("Files and Directories in '% s':" % path)
# for entry in obj:
#     if entry.is_file():
#         print(entry.name)

#pip install pdf2image
# import os
# import tempfile
# from pdf2image import convert_from_path
# output_folder=os.getcwd() #current work directory

# def pdf_to_png(pdf_name,source,destino):
#     with tempfile.TemporaryDirectory() as path:
#             images_from_path = convert_from_path(pdf_path=source+"/"+pdf_name,
#             dpi=100,
#             output_folder=destino,
#             fmt="png",
#             output_file=pdf_name[:-4],
#             single_file=True)
            
# for filename in os.listdir(output_folder):
#     if filename.endswith(".pdf"):
#         pdf_to_png(filename,output_folder,output_folder)

# print("ok!")





# importing required modules
# import PyPDF2
# import pyttsx3
  
# # path of the PDF file
# path = open('Gray Hat Hacking and Complete Guide to Hacking.pdf', 'rb')
  
# # creating a PdfFileReader object
# pdfReader = PyPDF2.PdfFileReader(path)
  
# # the page with which you want to start
# # this will read the page of 25th page.c
# from_page = pdfReader.getPage(24)
  
# # extracting the text from the PDF
# text = from_page.extractText()
  
# # reading the text
# speak = pyttsx3.init()
# speak.say(text)
# speak.runAndWait()


# import camelot

# # replace with a valid path on your local filesystem
# PDF_FILE_PATH = "Beginning C++17, 5th Edition.pdf"

# # raises an exception from PyPDF2
# camelot.read_pdf(PDF_FILE_PATH)








# 





import glob

# Folder path where the PDF files are located
folder_path = './pdf_file_listing/pdf_file_listing/Content/'
# Search for PDF files in the folder
pdf_files = glob.glob(folder_path + '/*.pdf')
# Print the list of PDF files
for file_path in pdf_files:
    # to remove ./ infront of file name
    cleaned_file_name = file_path.lstrip(folder_path)
    print(cleaned_file_name)
