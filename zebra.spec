Summary:	Routing daemon
Name:		zebra
Version:	0.74
Release:	0.1
Copyright:	GPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.zebra.org/pub/zebra/%{name}-%{version}.tar.gz
Source1:	zebra.conf
Source2:	zebra-bgpd.conf
Source3:	zebra-ospf6d.conf
Source4:	zebra-ospfd.conf
Source5:	zebra-ripd.conf
Source6:	zebra-ripngd.conf
Source7:	zebra.init
Source8:	zebra.sysconfig
Source9:	zebra.log
Patch:		zebra-info.patch
URL:		http://www.zebra.org/
BuildRequires:	texinfo
BuildRequires:	info
BuildRequires:	autoconf
BuildRequires:	guile-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
Prereq:		/sbin/install-info
Prereq:		/sbin/chkconfig
#Obsoletes:	mrt
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_sysconfdir /etc/%{name}

%description
Zebra is a multi-server routing software package which provides TCP/IP based
routing protocols also with IPv6 support such as RIP, OSPF, BGP and so on.
Zebra turns your machine into a full powered router.

%description -l pl
Program do dynamicznego ustawiania tablicy tras.
Mo¿e tak¿e ustalaæ trasy dla IPv6.

%package guile
Summary:	Guile interface for zebra routing daemon
Summary:	Guile dla programu zebra
Group:          Networking/Daemons
Group(pl):      Sieciowe/Serwery
Requires:	%{name} = %{version}

%description
Guile interface for zebra routing daemon.

%description guile -l pl
Guile dla programu zebra.

%prep
%setup -q -n %{name}-%{version}
%patch -p1

if [ -d /proc/sys/net/ipv6 ]; then
	echo "Yor system support ipv6"
else
	echo "Yor system doesn't support ipv6"
	exit 1
fi

%build
#autoconf
LDFLAGS="-s"; export LDFLAGS 
%configure #\
#	--enable-guile

make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig,logrotate.d} \
	$RPM_BUILD_ROOT/var/log/zebra

make install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/zebra.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/bgpd.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/ospf6d.conf
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/ospfd.conf
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/ripd.conf
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/ripngd.conf
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/zebra
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/zebra
install %{SOURCE9} $RPM_BUILD_ROOT/etc/logrotate.d/zebra

touch $RPM_BUILD_ROOT/var/log/zebra/zebra.log
touch $RPM_BUILD_ROOT/var/log/zebra/bgpd.log
touch $RPM_BUILD_ROOT/var/log/zebra/ospf6d.log
touch $RPM_BUILD_ROOT/var/log/zebra/ospfd.log
touch $RPM_BUILD_ROOT/var/log/zebra/ripd.log
touch $RPM_BUILD_ROOT/var/log/zebra/ripngd.log

gzip -9nf README AUTHORS NEWS ChangeLog tools/* \
	$RPM_BUILD_ROOT%{_infodir}/* 

%post
/sbin/install-info %{_infodir}/%{name}.info.gz /etc/info-dir >&2
/sbin/chkconfig --add zebra >&2
touch /var/log/zebra/zebra.log
touch /var/log/zebra/bgpd.log
touch /var/log/zebra/ospf6d.log
touch /var/log/zebra/ospfd.log
touch /var/log/zebra/ripd.log
touch /var/log/zebra/ripngd.log

if [ -f /var/run/zebra.pid ]; then
	/etc/rc.d/init.d/zebra restart >&2
else
	echo "Run '/etc/rc.d/init.d/zebra start' to start routing deamon." >&2
fi
    
%preun
if [ "$1" = "0" ]; then
        /sbin/install-info --delete %{_infodir}/%{name}.info.gz \
		/etc/info-dir >&2
	/etc/rc.d/init.d/zebra stop >&2
        /sbin/chkconfig --del zebra >&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tools/*
%{_infodir}/*info*
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/*
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/sysconfig/*
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/logrotate.d/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*.conf
%dir %attr(750,root,root) /var/log/zebra
%ghost /var/log/zebra/*

%files guile
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/*
