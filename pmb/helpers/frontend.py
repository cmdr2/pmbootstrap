#!/usr/bin/env python3

"""
Copyright 2017 Oliver Smith

This file is part of pmbootstrap.

pmbootstrap is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pmbootstrap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pmbootstrap.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import pmb.aportgen
import pmb.build
import pmb.config
import pmb.challenge
import pmb.chroot
import pmb.chroot.initfs
import pmb.chroot.other
import pmb.flasher
import pmb.helpers.logging
import pmb.helpers.other
import pmb.helpers.run
import pmb.install
import pmb.parse


def aportgen(args):
    pmb.aportgen.generate(args, args.package)


def build(args):
    pmb.build.package(args, args.package, args.arch, args.force,
                      args.buildinfo)


def build_init(args):
    pmb.build.init(args, args.suffix)


def challenge(args):
    pmb.challenge.frontend(args)


def checksum(args):
    pmb.build.checksum(args, args.package)


def chroot(args):
    pmb.chroot.apk.check_min_version(args, args.suffix)
    pmb.chroot.root(args, args.command, args.suffix, log=False)


def index(args):
    pmb.build.index_repo(args)


def initfs(args):
    pmb.chroot.initfs.frontend(args)


def install(args):
    pmb.install.install(args)


def flasher(args):
    pmb.flasher.frontend(args)


def menuconfig(args):
    pmb.build.menuconfig(args, args.package, args.deviceinfo["arch"])


def parse_apkbuild(args):
    aport = pmb.build.other.find_aport(args, args.package)
    path = aport + "/APKBUILD"
    print(json.dumps(pmb.parse.apkbuild(args, path), indent=4))


def parse_apkindex(args):
    result = pmb.parse.apkindex.parse(args, args.apkindex_path)
    print(json.dumps(result, indent=4))


def shutdown(args):
    pmb.chroot.shutdown(args)


def stats(args):
    pmb.build.ccache_stats(args, args.arch)


def log(args):
    pmb.helpers.run.user(args, ["tail", "-f", args.log, "-n", args.lines],
                         log=False)


def log_distccd(args):
    logpath = "/home/user/distccd.log"
    pmb.chroot.user(args, ["tail", "-f", logpath, "-n", args.lines], log=False)


def zap(args):
    pmb.chroot.zap(args)
