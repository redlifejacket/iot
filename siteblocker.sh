#!/bin/bash
# Shyam Govardhan
# 27 May 2018
# UCI IOT Networking & Security Week 7 Assignment

allow="allow"
deny="deny"
function usage {
  echo "Usage: $0 <${allow}|${deny}> <domain>"
  exit
}

[[ $# -ne 2 ]] && usage
[[ "$1" != "${allow}" && "$1" != "${deny}" ]] && usage
command=$1

domain=$2
ipaddr=$(getent hosts ${domain} | awk '{ print $1 }')
web_browser=/usr/bin/chromium-browser
domain=$2

function openWebBrowser {
  echo -n "killing ${web_browser}... "
  killall ${web_browser}
  echo "done"
  echo -n "Clearing ${web_browser} cache... "
  rm -rf  ${HOME}/.cache/Chromium/Default/Cache/*
  echo "done"
  echo -n "Launching ${web_browser} with ${url}  "
  ${web_browser} ${url} &
  echo "done"
}

function isUrlAccessible {
  local __resultvar=$1
  local url=$2
  echo "isUrlAccessible($url) executing..."
  #wget -q ${url}
  timeout 3s curl -fIsS ${url} > /dev/null
  if [ $? -eq 0 ]
  then
    status="UNBLOCKED"
    __resultvar=true
  else
    status="BLOCKED"
    __resultvar=false
  fi
  echo "${url} is ${status}!"
}

function addFirewallRule {
  cmd=$1
  ip=$2
  port=$3
  sudocmd="sudo ufw ${cmd} out to ${ipaddr} port ${port}"
  echo ${sudocmd}
  eval ${sudocmd}
}

# Main program
date
sudo ufw reset
sudo ufw enable
addFirewallRule $command ${ipaddr} 80
addFirewallRule $command ${ipaddr} 443
sudo ufw reload
isUrlAccessible site_status "http://${domain}"
[[ "${site_status}" = true ]] && openWebBrowser "http://${domain}"
isUrlAccessible site_status "https://${domain}"
[[ "${site_status}" = true ]] && openWebBrowser "https://${domain}"
date
