Summary: Gluster 3.12 (Long Term Stable) packages from the CentOS Storage SIG repository
Name: centos-release-gluster312
Version: 0.9
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-3.12.repo

BuildArch: noarch

# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

Provides: centos-release-gluster = 3.12

# Obsoletes: for 3.11 (STM) only, 3.11 is EOL when 3.12 is released
Obsoletes: centos-release-gluster311
# No Conflicts:, possibly older repositories contain additional tools and those
# are still expected to be working.

%description
yum configuration for Gluster 3.12 packages from the CentOS Storage SIG.
Gluster 3.12 is a Long Term Stable release and will receive updates for 12
months. For more details about the Long Term Stable and Short Term Stable
release schedule, see https://www.gluster.org/community/release-schedule

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.12.repo

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.12.repo

%changelog
* Sat Aug 12 2017 Niels de Vos <ndevos@redhat.com> - 0.9-1
- Initial version based on centos-release-gluster310
