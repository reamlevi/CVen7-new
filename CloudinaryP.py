import cloudinary
from cloudinary import uploader

"""UploadPic-------------------------------------------------------------------------------------------------------------------------------------------"""
cloudinary.config(
    cloud_name="ds6uapscn",
    api_key="132635951351588",
    api_secret="V2dCOsRXYgQvigq9UmiRSF4nvho")


def upload(pic, id):

    """
    >>> upload("TestPic.jpg",123456789)
    'http://res.cloudinary.com/ds6uapscn/image/upload/v1515224361/123456789.jpg'
    """

    jp = cloudinary.uploader.upload(pic, public_id=id)
    return jp['url']
