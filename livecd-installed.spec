Summary:	PLD LiveCD scripts for installed LiveCD
Summary(pl.UTF-8):	Skrypty PLD LiveCD dla zainstalowanego LiveCd
Name:		livecd-installed
Version:	1.91
Release:	1
License:	GPL
Group:		Base
Source0:	http://ep09.pld-linux.org/~havner/livecd-%{version}.tar.bz2
# Source0-md5:	a5fff13c0dda53b1669715dd03f52bfd
PreReq:		rc-scripts
Requires:	livecd-common
Obsoletes:	livecd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scripts for PLD LiveCD:
- init script

%description -l pl.UTF-8
Skrypty dla PLD LiveCD
- skrypt init

%prep
%setup -q -n livecd-1.91

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

install rc.live $RPM_BUILD_ROOT/etc/rc.d/rc.live

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/rc.live
