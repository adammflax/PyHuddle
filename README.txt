PyHuddle
========
PyHuddle is a module that attempts to abstract away the wire protocol. The problem with hard coded URI's is that they may change.
The only URI that you can rely on is the one you just got from the server. Huddle provides means of navigating between workspaces and folders and documents
by navigating the links that get returned in the folders structure. PyHuddle uses this navigation to work so no matter what changes on the backend
your front end application should still work. Furthermore PyHuddle does not depend on any HTTP library. Simply plug in your HTTP library of choice, 
and create a HTTPAdapter by extending the Adapter class. Look at HTTPlib2Adapter which is an adapter for the HTTPlib2 library on an example of how 
to do this

PyHuddle supports the following:

1. OAuth with OOB. The HandleAccessToken class will manage retriving, saving, and refreshing of your tokens.
2. Full access to the folder Api
3. Full access to the documents Api
4. Full access to the workspace Api
5. Full access to the user + actor Api 
6. Full access to the workspace calandars api (Workspace Calandar)
7. Full access to the tasks Api

Setup
=====
Setup is simple. 
Create your OAuth details by [contacting Huddle](https://code.google.com/p/huddle-apis/wiki/OauthIntegration#Registering_your_client)

Create a .ini File that looks like this
```
[OAUTH2]
redirectUri = 
clientID = 
clientSecret =

[OAUTH2ENDPOINT]
huddleAuthServer = http://login.huddle.net/
huddleAccessTokenServer =  http://login.huddle.dev/net/

[API]
accept = application/vnd.huddle.data+json 
huddleApiServer = http://api.huddle.net/
huddleCalandarServer = http://api.huddle.net/v2/calendar/workspaces/
huddleTaskServer = http://api.huddle.net/v2/calendar/events/
```

If you are not using OOB for OAuth this isn't much of a problem. You simply need to create your own getAccessToken function
and then when you instantiate the handleAccessToken class you can plug in your function there

Usage
====
```
adapter = AdapterHttpUrlLib() #your http library implementation
config = Config("filePath").config #reads your config file
tokenHandler = HandleAccessToken(adapter, config) #gets you an access token looks at file, if can't find grabs from web, looks to see if expired
client = HuddleClient(tokenHandler, adapter, config) #start our api and hit /entry/

#get your workspaces
workSpaceList = client.getWorkspaces()
#get the 1st folder in the 4th workspace
folder = workSpaceList.getWorkspaceEntry().getFolders()[0]
#get a document
document = folder.getDocuments[0]
```

```
#delete the folder
folder.deleteFolder()
#restore the folder
folder.restoreFolder()
#move the folder
folder.moveTo(folderB obj)
#download the document
document.download()
#upload a new version of the document
document.uploadNewVersion(fileObject)
```

you get the idea

