import admin

steve = admin.Admin('steve', 'smith', 'coral springs', 67)
steve.privileges.show_privileges()

steve_privileges = ['change passwords', 'delete accounts']

steve.privileges.privileges = steve_privileges
steve.privileges.show_privileges()
