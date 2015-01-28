%global cartridgedir %{_libexecdir}/openshift/cartridges/nginx-hhvm
%global frameworkdir %{_libexecdir}/openshift/cartridges/nginx-hhvm

Name:          openshift-cartridge-nginx-hhvm
Version:       1.0.0.0
Release:       1%{?dist}
Summary:       Nginx HHVM WordPress cartridge
Group:         Development/Languages
License:       GNU GPL 3.0
URL:           https://github.com/AbhishekGhosh/OpenShift-Nginx-HHVM-WordPress-Multisite
Source0:       https://github.com/AbhishekGhosh/origin-server/%{name}/%{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)

%description
Nginx HHVM WordPress cartridge for openshift. (Cartridge Format V2)

%prep
%setup -q

%build

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__mkdir -p %{buildroot}%{cartridgedir}/versions/shared/configuration/etc/conf/

%files
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md


%changelog
* huh?
