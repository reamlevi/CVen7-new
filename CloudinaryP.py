import cloudinary
from cloudinary import uploader
"""UploadPic-------------------------------------------------------------------------------------------------------------------------------------------"""
cloudinary.config(
  cloud_name = "ds6uapscn",
  api_key = "132635951351588",
  api_secret = "V2dCOsRXYgQvigq9UmiRSF4nvho")

def upload(pic,id):
    jp= cloudinary.uploader.upload(pic,public_id=id)
    return jp

def show(pic):
    cloudinary.CloudinaryImage(pic).image(alt="Sample Image")

