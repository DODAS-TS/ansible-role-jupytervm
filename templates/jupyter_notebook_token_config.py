from s3contents import S3ContentsManager

c = get_config()

c.NotebookApp.token = "{{ jupyter_token }}"
c.NotebookApp.notebook_dir = '/opt/notebooks'