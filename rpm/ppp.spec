Name: pppd-headers
Version: 2.4.7
Release: 0
Summary: Header files for pppd
Group: Development/Libraries
BuildArch: noarch
License: BSD
URL: http://git.ozlabs.org
Source: %{name}-%{version}.tar.bz2

%description
Header files for pppd

%prep
%setup -q -n %{name}-%{version}/ppp

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_includedir}/pppd
cp pppd/*.h %{buildroot}%{_includedir}/pppd

%files
%defattr(-,root,root,-)
%{_includedir}/pppd
