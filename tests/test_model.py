# -*- coding: utf-8 -*-
# (c) 2022 The mqttwarn developers
from copy import deepcopy

from mqttwarn.core import Job, make_service

JOB_PRIO1 = dict(
    prio=1, service="service", section="section", topic="topic", payload="payload", data="data", target="target"
)
JOB_PRIO2 = dict(
    prio=2, service="service", section="section", topic="topic", payload="payload", data="data", target="target"
)
JOB_PRIO1_COPY = deepcopy(JOB_PRIO1)


def test_make_service():
    """
    Verify creation of `Service` instance.
    """
    service = make_service(name="foo")
    assert "<mqttwarn.core.Service object at" in str(service)


def test_job_equality():
    """
    Test comparing `Job` instances for equality.
    """
    job1 = Job(**JOB_PRIO1)
    job2 = Job(**JOB_PRIO1_COPY)

    assert job1 == job2


def test_job_inequality():
    """
    Test comparing `Job` instances for inequality.
    """
    job1 = Job(**JOB_PRIO1)
    job2 = Job(**JOB_PRIO2)

    assert job1 != job2


def test_job_ordering_by_priority():
    """
    Test sorting a list of `Job` instances by priority.
    """
    job1 = Job(**JOB_PRIO1)
    job2 = Job(**JOB_PRIO2)

    assert sorted([job2, job1]) == [job1, job2]