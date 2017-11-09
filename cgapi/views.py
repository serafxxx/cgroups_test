# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.views import APIView
from cgroups import Cgroup
from cgroups.common import CgroupsException

from cgapi.serializers import CgroupSerializer
from cgroups_test.common import CgroupsError


class CgroupAPIView(APIView):
    """Create new cgroup / list processes of given cgroup"""

    def get(self, request, cgname):
        """List processes from the given group. Create new one if no such group."""
        try:
            cg = Cgroup(cgname)
            serializer = CgroupSerializer(cg)
            data = serializer.data
        except CgroupsException as e:
            raise CgroupsError(e)

        return Response(data)


class PidAPIView(APIView):
    """Add given process by PID into the given cgroup (could be new)."""

    def put(self, request, cgname, pid):
        """Add process to the cgroup and return a list of processes in the group"""

        try:
            # Init or create cgroup
            cg = Cgroup(cgname)
            # Add process to the group
            # For security reasons you have to be root or the process has to
            # belong to user under which you're running this api.
            cg.add(int(pid))

            serializer = CgroupSerializer(cg)
            data = serializer.data
        except CgroupsException as e:
            raise CgroupsError(e)

        return Response(data)
