from s3contents import S3ContentsManager

c = get_config()

c.NotebookApp.token = "{{ jupyter_token }}"

# Tell Jupyter to use S3ContentsManager for all storage.
c.NotebookApp.contents_manager_class = S3ContentsManager
c.S3ContentsManager.access_key_id = "{{ s3_access_id}}"
c.S3ContentsManager.secret_access_key = "{{ s3_access_key }}"
c.S3ContentsManager.endpoint_url = "{{ s3_endpoint }}"
c.S3ContentsManager.bucket = "{{ s3_bucket }}"
c.S3ContentsManager.prefix = "{{ s3_mount_prefix }}"