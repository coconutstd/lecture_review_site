from storages.backends.s3boto3 import S3Boto3Storage

# for static files
class S3StaticStorage(S3Boto3Storage):
    location = 'static'


# for media files
class S3MediaStorage(S3Boto3Storage):
    location = 'media'

