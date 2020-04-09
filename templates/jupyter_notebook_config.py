from s3contents import S3ContentsManager
from hybridcontents import HybridContentsManager
from IPython.html.services.contents.filemanager import FileContentsManager

c = get_config()

c.NotebookApp.token = "{{ jupyter_token }}"

c.NotebookApp.contents_manager_class = HybridContentsManager

c.HybridContentsManager.manager_classes = {
    # Associate the root directory with an S3ContentsManager.
    # This manager will receive all requests that don"t fall under any of the
    # other managers.
    "shared_notebooks": S3ContentsManager,
    # Associate /directory with a FileContentsManager.
    "": FileContentsManager,
}

c.HybridContentsManager.manager_kwargs = {
    # Args for root S3ContentsManager.
    "shared": {
        "access_key_id": "{{ s3_access_id}}",
        "secret_access_key": "{{ s3_access_key }}",
        "endpoint_url": "{{ s3_endpoint }}",
        "bucket": "{{ s3_bucket }}",
    },
    # Args for the FileContentsManager mapped to /directory
    "": {
        "root_dir": "/opt/cloudadm",
    },
}
