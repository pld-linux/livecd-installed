Summary:	PLD LiveCD scripts for installed LiveCD
Summary(pl):	Skrypty PLD LiveCD dla zainstalowanego LiveCd
Name:		livecd-installed
Version:	1.0
Release:	1
License:	GPL
Group:		Base
Source0:	http://ep09.pld-linux.org/~havner/livecd-%{version}.tar.bz2
# Source0-md5:	f0bc5023d278c3c39dcdbca9e9539c78
PreReq:		rc-scripts
Requires:	livecd-common
Obsoletes:	livecd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scripts for PLD LiveCD:
- init script

%description -l pl
Skrypty dla PLD LiveCD
- skrypt init

%prep
%setup -q -n livecd

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_initrddir}

install rc.live-installed $RPM_BUILD_ROOT/etc/rc.d/rc.live

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/rc.live
