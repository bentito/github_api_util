#!/usr/bin/env python

from requests.auth import HTTPBasicAuth
import requests
import os

GIT_USER = os.environ['GIT_USER']
GIT_TOKEN = os.environ['GIT_TOKEN']

opr_framework_repo_list = \
    [
        "operator-framework/operator-metering",
        "operator-framework/operator-lifecycle-manager",
        "operator-framework/helm-app-operator-kit",
        "operator-framework/operator-sdk",
        "operator-framework/operator-sdk-samples",
        "operator-framework/awesome-operators",
        "operator-framework/operator-manifests",
        "operator-framework/getting-started",
        "operator-framework/operator-marketplace",
        "operator-framework/olm-broker",
        "operator-framework/go-appr",
        "operator-framework/helm",
        "operator-framework/jmx_exporter",
        "operator-framework/hive",
        "operator-framework/hadoop",
        "operator-framework/operator-registry",
        "operator-framework/mock-extension-apiserver",
        "operator-framework/grpc-health-probe",
        "operator-framework/operator-courier",
        "operator-framework/community-operators",
        "operator-framework/operatorhub.io",
        "operator-framework/presto",
        "operator-framework/operatorhub-docs",
        "operator-framework/ghostunnel",
        "operator-framework/api",
        "operator-framework/bigdata-interop",
        "operator-framework/olm-book",
        "operator-framework/community",
        "operator-framework/enhancements",
        "operator-framework/operator-sdk-ansible-util"
    ]

try:
    team_check_manages_repo_uri = "https://api.github.com/orgs/operator-framework/teams/team-metering/repos/"
    for org_repo in opr_framework_repo_list:
        r = requests.get(team_check_manages_repo_uri + org_repo, auth=HTTPBasicAuth(GIT_USER, GIT_TOKEN))
        print '%-50s  %s' % (org_repo, r.status_code)
except requests.ConnectionError:
    print("failed to connect")
