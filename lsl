gitpod /workspace/Black (REST_DEVELOP) $ docker build -t black .
[+] Building 29.3s (13/16)                                                                            
 => [internal] load .dockerignore                                                                0.0s
 => => transferring context: 2B                                                                  0.0s
 => [internal] load build definition from Dockerfile                                             0.0s
 => => transferring dockerfile: 1.40kB                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.10.4                                 0.6s
 => [internal] load build context                                                                0.0s
 => => transferring context: 10.17kB                                                             0.0s
 => [ 1/12] FROM docker.io/library/python:3.10.4@sha256:cddebe04ec7846e28870cf8624b46313a22e640  0.0s
 => CACHED [ 2/12] WORKDIR /black                                                                0.0s
 => CACHED [ 3/12] RUN apt-get update && apt-get install -y locales locales-all                  0.0s
 => CACHED [ 4/12] RUN locale-gen fa_IR.UTF-8                                                    0.0s
 => [ 5/12] COPY . .                                                                             0.2s
 => [ 6/12] RUN pip install -r requirements.txt                                                 17.0s
 => [ 7/12] RUN python -m venv venv                                                              3.6s
 => [ 8/12] RUN source venv/bin/activate                                                         0.5s 
 => ERROR [ 9/12] RUN python3 manage.py makemigrations --empty index && python3 manage.py makem  7.3s 
------                                                                                                
 > [ 9/12] RUN python3 manage.py makemigrations --empty index && python3 manage.py makemigrations --empty blog && python3 manage.py makemigrations --empty product && python3 manage.py makemigrations user_accounts && python3 manage.py makemigrations index && python3 manage.py makemigrations product && python3 manage.py makemigrations blog:                                                                    
#0 1.839 Migrations for 'index':                                                                      
#0 1.839   index/migrations/0001_initial.py
#0 3.125 Migrations for 'blog':
#0 3.125   blog/migrations/0001_initial.py
#0 4.373 Migrations for 'product':
#0 4.373   product/migrations/0001_initial.py
#0 5.643 Migrations for 'user_accounts':
#0 5.643   user_accounts/migrations/0001_initial.py
#0 5.643     - Create model user_accounts
#0 6.894 Traceback (most recent call last):
#0 6.894   File "/black/manage.py", line 22, in <module>
#0 6.894     main()
#0 6.894   File "/black/manage.py", line 18, in main
#0 6.895     execute_from_command_line(sys.argv)
#0 6.895   File "/usr/local/lib/python3.10/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
#0 6.895     utility.execute()
#0 6.895   File "/usr/local/lib/python3.10/site-packages/django/core/management/__init__.py", line 436, in execute
#0 6.895     self.fetch_command(subcommand).run_from_argv(self.argv)
#0 6.895   File "/usr/local/lib/python3.10/site-packages/django/core/management/base.py", line 412, in run_from_argv
#0 6.895     self.execute(*args, **cmd_options)
#0 6.895   File "/usr/local/lib/python3.10/site-packages/django/core/management/base.py", line 458, in execute
#0 6.895     output = self.handle(*args, **options)
#0 6.895   File "/usr/local/lib/python3.10/site-packages/django/core/management/base.py", line 106, in wrapper
#0 6.895     res = handle_func(*args, **kwargs)
#0 6.895   File "/usr/local/lib/python3.10/site-packages/django/core/management/commands/makemigrations.py", line 137, in handle
#0 6.895     loader = MigrationLoader(None, ignore_no_migrations=True)
#0 6.895   File "/usr/local/lib/python3.10/site-packages/django/db/migrations/loader.py", line 58, in __init__
#0 6.895     self.build_graph()
#0 6.895   File "/usr/local/lib/python3.10/site-packages/django/db/migrations/loader.py", line 305, in build_graph
#0 6.895     self.graph.ensure_not_cyclic()
#0 6.895   File "/usr/local/lib/python3.10/site-packages/django/db/migrations/graph.py", line 284, in ensure_not_cyclic
#0 6.896     raise CircularDependencyError(
#0 6.896 django.db.migrations.exceptions.CircularDependencyError: wagtailcore.0063_modellogentry, wagtailcore.0064_log_timestamp_indexes, wagtailcore.0065_log_entry_uuid, wagtailcore.0066_collection_management_permissions, wagtailcore.0067_alter_pagerevision_content_json, wagtailcore.0068_log_entry_empty_object, wagtailcore.0069_log_entry_jsonfield, wagtailcore.0070_rename_pagerevision_revision, wagtailcore.0071_populate_revision_content_type, wagtailcore.0072_alter_revision_content_type_notnull, wagtailcore.0073_page_latest_revision, wagtailcore.0074_revision_object_str, wagtailcore.0075_populate_latest_revision_and_revision_object_str, wagtailcore.0076_modellogentry_revision, wagtailcore.0077_alter_revision_user, wagtailcore.0078_referenceindex, wagtailcore.0079_rename_taskstate_page_revision, wagtailcore.0080_generic_workflowstate, wagtailcore.0081_populate_workflowstate_content_type, wagtailcore.0082_alter_workflowstate_content_type_notnull, wagtailcore.0083_workflowcontenttype, user_accounts.0001_initial
------
Dockerfile:33
--------------------
  31 |     
  32 |     # Run migrations
  33 | >>> RUN python3 manage.py makemigrations --empty index && python3 manage.py makemigrations --empty blog && python3 manage.py makemigrations --empty product && python3 manage.py makemigrations user_accounts && python3 manage.py makemigrations index && python3 manage.py makemigrations product && python3 manage.py makemigrations blog
  34 |     RUN python3 manage.py migrate
  35 |     
--------------------
ERROR: failed to solve: process "/bin/bash -c python3 manage.py makemigrations --empty index && python3 manage.py makemigrations --empty blog && python3 manage.py makemigrations --empty product && python3 manage.py makemigrations user_accounts && python3 manage.py makemigrations index && python3 manage.py makemigrations product && python3 manage.py makemigrations blog" did not complete successfully: exit code: 1