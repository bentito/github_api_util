Before using this Python code you must:

`export GIT_USER=<your git user with team permissions for team you want to see about management capabilities>`

`export GIT_TOKEN=<personal access token for GIT_USER, make one if you don't have one. scope as needed>`

`pip install requests`
`chmod u+x getOprFwkTeamMeteringMgmtPerms.py`

run as: 

`getOprFwkTeamMeteringMgmtPerms.py`

Output is 204 for repos your team manages, 404 if not.

> *Note:* list of repos as of Feb-7-2020 for operator-framework org is hard coded as list at start of this script.
