Summary:	Routing daemon
Name:		zebra
Version:	0.91a
Release:	4
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.zebra.org/pub/zebra/%{name}-%{version}.tar.gz
Source1:	%{name}.conf
Source2:	%{name}-bgpd.conf
Source3:	%{name}-ospf6d.conf
Source4:	%{name}-ospfd.conf
Source5:	%{name}-ripd.conf
Source6:	%{name}-ripngd.conf
Source7:	Zebra.conf
Source8:	vtysh.conf
Source9:	%{name}.init
Source10:	%{name}.sysconfig
Source11:	%{name}.logrotate
Patch0:		%{name}-info.patch
Patch1:		%{name}-proc.patch
Patch2:		%{name}-socket_paths.patch
URL:		http://www.zebra.org/
BuildRequires:	texinfo
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.1
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	ucd-snmp-devel >= 4.2.1
Prereq:		rc-scripts
Provides:	routingdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	bird
Obsoletes:	gated
Obsoletes:	mrt

%define		_sysconfdir /etc/%{name}

%description
Zebra is a multi-server routing software package which provides TCP/IP
based routing protocols also with IPv6 support such as RIP, OSPF, BGP
and so on. Zebra turns your machine into a full powered router.

%description -l pl
Program do dynamicznego ustawiania tablicy tras. Mo�e tak�e ustala�
trasy dla IPv6.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
aclocal
autoconf
automake -a -c
%configure \
	--enable-one-vty \
	--enable-ipv6 \
	--enable-netlink \
	--enable-snmp \
	--enable-vtysh

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig,logrotate.d} \
	$RPM_BUILD_ROOT/var/log/{archiv,}/zebra \
	$RPM_BUILD_ROOT/var/run/zebra 

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/zebra.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/bgpd.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/ospf6d.conf
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/ospfd.conf
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/ripd.conf
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/ripngd.conf
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/Zebra.conf
install %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/vtysh.conf
install %{SOURCE9} $RPM_BUILD_ROOT/etc/rc.d/init.d/zebra
install %{SOURCE10} $RPM_BUILD_ROOT/etc/sysconfig/zebra
install %{SOURCE11} $RPM_BUILD_ROOT/etc/logrotate.d/zebra

touch $RPM_BUILD_ROOT/var/log/zebra/{zebra,bgpd,ospf6d,ospfd,ripd,ripngd}.log

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/chkconfig --add zebra >&2
touch $RPM_BUILD_ROOT/var/log/zebra/{zebra,bgpd,ospf6d,ospfd,ripd,ripngd}.log

if [ -f /var/lock/subsys/zebra ]; then
	/etc/rc.d/init.d/zebra restart >&2
else
	echo "Run '/etc/rc.d/init.d/zebra start' to start routing deamon." >&2
fi
    
%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/zebra ]; then
		/etc/rc.d/init.d/zebra stop >&2
	fi
        /sbin/chkconfig --del zebra >&2
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS ChangeLog tools/*
%{_infodir}/*info*
%{_mandir}/man*/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%attr(754,root,root) /etc/rc.d/init.d/*
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/sysconfig/*
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/logrotate.d/*
%config(noreplace) %verify(not size mtime md5) %attr(640,root,root) %{_sysconfdir}/*.conf
%dir %attr(750,root,root) /var/run/zebra
%dir %attr(750,root,root) /var/log/zebra
%dir %attr(750,root,root) /var/log/archiv/zebra
%ghost /var/log/zebra/*
