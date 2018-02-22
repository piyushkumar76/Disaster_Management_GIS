from pip import main
package_list = ['django','django-rest-framework','geopy','python-socketio']
for i in package_list:
    main(['install',i])
