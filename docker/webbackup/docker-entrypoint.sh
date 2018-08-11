#!/bin/bash
#
# Copyright (C) 2017 Google Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

set -e

echo >&2 'Starting webbackup build.'
cd /app/webbackup
echo >&2 'Cloning repositories.'
pwd
git clone https://github.com/fgms/webbackup.git
git clone https://github.com/sturple/pycloud.git
echo>&2 'Setting permisions.'
chmod +x /app/webbackup/webbackup/webbackup.py
pip3 install -e pycloud 1>/dev/null
cd /app/webbackup/webbackup
python3 webbackup.py --config /app/config/web_backups.cfg
echo >&2 'Finsihed'

exec "$@"
