# import os
# import fitz  # PyMuPDF

# pdf_file = "pdff.pdf"
# output_directory = "extracted_content"
# os.makedirs(output_directory, exist_ok=True)

# print(fitz.__version__)

# try:
#     with fitz.open(pdf_file) as doc:
#         text_content = ""
#         image_files = []
#         for page_num in range(len(doc)):
#             page = doc[page_num]
#             # print(page.get_images(full=False))
#             print(page.get_images(full=True))
#             text_content += page.get_text("text")

#             image_list = page.get_images(full=True)

#             for img_index, img in enumerate(image_list, start=1):
#                 xref = img[0]
#                 ext = img[2]
#                 img_bytes = doc.extract_image(xref)["image"]

#                 img_filename = f"page_{page_num+1}_image_{img_index}.{ext}"
#                 with open(img_filename, "wb") as f:
#                     f.write(img_bytes)
#                 image_files.append(img_filename)

# except Exception as e:
#     # print(e)
#     pass


# # extracted_text, extracted_images = extract_content_from_pdf(
# #     pdf_file, output_directory)

# # if extracted_text:
# #     print("Text extracted successfully!")
# #     print("Extracted Text:\n", extracted_text)  # Print a snippet

# # if extracted_images:
# #     print("Images extracted successfully!")
# #     print("Extracted Image Files:", extracted_images)
