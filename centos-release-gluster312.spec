Summary: Gluster 3.12 (Long Term Stable) packages from the CentOS Storage SIG repository
Name: centos-release-gluster312
Version: 1.0
Release: 2%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-3.12.repo

BuildArch: noarch

%if 0%{?centos} >= 7
# $contentdir for altarch support was added with CentOS-7.5
Requires: centos-release >= 7-5.1804.el7.centos.2
%endif
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
%if 0%{?centos} < 7
sed -i 's/i\$contentdir/centos/g' %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.12.repo
%endif

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.12.repo

%changelog
* Tue Jul 31 2018 Niels de Vos <ndevos@redhat.com> - 1.0-2
- Add support for altarch repositories

* Wed Aug 30 2017 Niels de Vos <ndevos@redhat.com> - 1.0-1
- Enable release repository, disable testing

* Sat Aug 12 2017 Niels de Vos <ndevos@redhat.com> - 0.9-1
- Initial version based on centos-release-gluster310
