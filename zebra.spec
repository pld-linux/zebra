#
# Conditional build:
%bcond_with	snmp	# with SNMP support (broken?)
#
Summary:	Routing daemon
Summary(pl.UTF-8):	Demon routingu
Summary(pt_BR.UTF-8):	Servidor de roteamento multi-protocolo
Summary(ru.UTF-8):	Демон маршрутизации Zebra
Summary(uk.UTF-8):	Демон маршрутизації Zebra
Name:		zebra
Version:	0.95a
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.zebra.org/pub/zebra/%{name}-%{version}.tar.gz
# Source0-md5:	9b8fec2d4f910334e50167414fcf193b
Source1:	%{name}.pam
Source10:	%{name}-zebra.init
Source11:	%{name}-bgpd.init
Source12:	%{name}-ospf6d.init
Source13:	%{name}-ospfd.init
Source14:	%{name}-ripd.init
Source15:	%{name}-ripngd.init
Source20:	%{name}-zebra.sysconfig
Source21:	%{name}-bgpd.sysconfig
Source22:	%{name}-ospf6d.sysconfig
Source23:	%{name}-ospfd.sysconfig
Source24:	%{name}-ripd.sysconfig
Source25:	%{name}-ripngd.sysconfig
Source30:	%{name}-zebra.logrotate
Source31:	%{name}-bgpd.logrotate
Source32:	%{name}-ospfd.logrotate
Source33:	%{name}-ospf6d.logrotate
Source34:	%{name}-ripngd.logrotate
Source35:	%{name}-ripd.logrotate
Patch0:		%{name}-proc.patch
Patch1:		%{name}-socket_paths.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-nolog.patch
URL:		http://www.zebra.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	pam-devel
BuildRequires:	readline-devel >= 4.1
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	texinfo
%{?with_snmp:BuildRequires:	ucd-snmp-devel >= 4.2.6}
Requires(post):	/bin/hostname
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
Provides:	routingdaemon
Obsoletes:	bird
Obsoletes:	gated
Obsoletes:	mrt
Obsoletes:	quagga
Obsoletes:	zebra-xs26
Conflicts:	logrotate < 3.7-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description
Zebra is a multi-server routing software package which provides TCP/IP
based routing protocols also with IPv6 support such as RIP, OSPF, BGP
and so on. Zebra turns your machine into a full powered router.

Daemons for each routing protocols are available in separate packages.

%description -l pl.UTF-8
Program do dynamicznego ustawiania tablicy tras. Może także ustalać
trasy dla IPv6.

Demony obsługujące poszczególne protokoły dostępne są w osobnych
pakietach.

%description -l pt_BR.UTF-8
Zebra é um servidor múltiplo para roteamento, provendo suporte aos
protocolos baseados em TCP/IP (inclusive IPv6) tais como RIP, OSPF,
BGP, entre outros. Zebra transforma sua máquina em um poderoso
roteador.

%description -l ru.UTF-8
GNU Zebra - это свободное программное обеспечение, работающее с
основанными на TCP/IP протоколами маршрутизации.

GNU Zebra поддерживает BGP4, BGP4+, OSPFv2, OSPFv3, RIPv1, RIPv2 и
RIPng.

%description -l uk.UTF-8
GNU Zebra - це вільне програмне забезпечення, що працює з базованими
на TCP/IP протоколами маршрутизації.

GNU Zebra підтримує BGP4, BGP4+, OSPFv2, OSPFv3, RIPv1, RIPv2 та
RIPng.

%package bgpd
Summary:	BGP routing daemon
Summary(pl.UTF-8):	Demon routingu BGP
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Obsoletes:	zebra-xs26-bgpd

%description bgpd
BGP routing daemon. Includes IPv6 support.

%description bgpd -l pl.UTF-8
Demon obsługi protokołu BGP. Obsługuje także IPv6.

%package ospfd
Summary:	OSPF routing daemon
Summary(pl.UTF-8):	Demon routingu OSPF
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description ospfd
OSPF routing daemon.

%description ospfd -l pl.UTF-8
Demon do obsługi protokołu OSPF.

%package ospf6d
Summary:	IPv6 OSPF routing daemon
Summary(pl.UTF-8):	Demon routingu OSPF w sieciach IPv6
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Obsoletes:	zebra-xs26-ospf6d

%description ospf6d
OSPF6 routing daemon for IPv6 networks.

%description ospf6d -l pl.UTF-8
Demon obsługi protokołu OSPF w sieciach IPv6.

%package ripd
Summary:	RIP routing daemon
Summary(pl.UTF-8):	Demon routingu RIP
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description ripd
RIP routing daemon for zebra.

%description ripd -l pl.UTF-8
Demon obsługi protokołu RIP.

%package ripngd
Summary:	IPv6 RIP routing daemon
Summary(pl.UTF-8):	Demon routingu RIP w sieciach IPv6
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Obsoletes:	zebra-xs26-ripngd

%description ripngd
RIP routing daemon for IPv6 networks.

%description ripngd -l pl.UTF-8
Demon obsługi protokołu RIP w sieciach IPv6.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%{__autoheader}
%configure \
	--enable-ipv6 \
	--enable-netlink \
	%{!?with_snmp:--disable-snmp} \
	%{?with_snmp:--enable-snmp} \
	--enable-vtysh \
	--with-libpam

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig,logrotate.d,pam.d} \
	$RPM_BUILD_ROOT/var/log/{archive,}/zebra \
	$RPM_BUILD_ROOT/var/run/zebra

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/zebra

install %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/zebra
install %{SOURCE11} $RPM_BUILD_ROOT/etc/rc.d/init.d/bgpd
install %{SOURCE12} $RPM_BUILD_ROOT/etc/rc.d/init.d/ospf6d
install %{SOURCE13} $RPM_BUILD_ROOT/etc/rc.d/init.d/ospfd
install %{SOURCE14} $RPM_BUILD_ROOT/etc/rc.d/init.d/ripd
install %{SOURCE15} $RPM_BUILD_ROOT/etc/rc.d/init.d/ripngd

install %{SOURCE20} $RPM_BUILD_ROOT/etc/sysconfig/zebra
install %{SOURCE21} $RPM_BUILD_ROOT/etc/sysconfig/bgpd
install %{SOURCE22} $RPM_BUILD_ROOT/etc/sysconfig/ospf6d
install %{SOURCE23} $RPM_BUILD_ROOT/etc/sysconfig/ospfd
install %{SOURCE24} $RPM_BUILD_ROOT/etc/sysconfig/ripd
install %{SOURCE25} $RPM_BUILD_ROOT/etc/sysconfig/ripngd

install %{SOURCE30} $RPM_BUILD_ROOT/etc/logrotate.d/zebra
install %{SOURCE31} $RPM_BUILD_ROOT/etc/logrotate.d/bgpd
install %{SOURCE32} $RPM_BUILD_ROOT/etc/logrotate.d/ospfd
install %{SOURCE33} $RPM_BUILD_ROOT/etc/logrotate.d/ospf6d
install %{SOURCE34} $RPM_BUILD_ROOT/etc/logrotate.d/ripd
install %{SOURCE35} $RPM_BUILD_ROOT/etc/logrotate.d/ripngd

touch $RPM_BUILD_ROOT/var/log/zebra/{zebra,bgpd,ospf6d,ospfd,ripd,ripngd}.log

touch $RPM_BUILD_ROOT%{_sysconfdir}/{vtysh.conf,zebra.conf}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/chkconfig --add zebra >&2
umask 027
if [ ! -s %{_sysconfdir}/zebra.conf ]; then
	echo "hostname `hostname`" > %{_sysconfdir}/zebra.conf
fi
%service zebra restart "main routing daemon"

%post bgpd
/sbin/chkconfig --add bgpd >&2
%service bgpd restart "bgpd routing daemon"

%post ospfd
/sbin/chkconfig --add ospfd >&2
%service ospfd restart "ospfd routing daemon"

%post ospf6d
/sbin/chkconfig --add ospf6d >&2
%service ospf6d restart "ospf6d routing daemon"

%post ripd
/sbin/chkconfig --add ripd >&2
%service ripd restart "ripd routing daemon"

%post ripngd
/sbin/chkconfig --add ripngd >&2
%service ripngd restart "ripngd routing daemon"

%preun
if [ "$1" = "0" ]; then
	%service zebra stop
	/sbin/chkconfig --del zebra >&2
fi

%preun bgpd
if [ "$1" = "0" ]; then
	%service bgpd stop
	/sbin/chkconfig --del bgpd >&2
fi

%preun ospfd
if [ "$1" = "0" ]; then
	%service ospfd stop
	/sbin/chkconfig --del ospfd >&2
fi

%preun ospf6d
if [ "$1" = "0" ]; then
	%service ospf6d stop
	/sbin/chkconfig --del ospf6d >&2
fi

%preun ripd
if [ "$1" = "0" ]; then
	%service ripd stop
	/sbin/chkconfig --del ripd >&2
fi

%preun ripngd
if [ "$1" = "0" ]; then
	%service ripngd stop
	/sbin/chkconfig --del ripngd >&2
fi

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README REPORTING-BUGS SERVICES TODO
%{_infodir}/*info*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
%dir %attr(750,root,root) %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{_sysconfdir}/*.conf
%attr(640,root,root) %{_sysconfdir}/*.sample*
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/zebra
%dir %attr(750,root,root) /var/run/zebra
%dir %attr(750,root,root) /var/log/zebra
%dir %attr(750,root,root) /var/log/archive/zebra

%doc zebra/*sample*
%{_mandir}/man8/zebra*
%attr(755,root,root) %{_sbindir}/zebra
%attr(754,root,root) /etc/rc.d/init.d/zebra
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/zebra
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/zebra
%ghost /var/log/zebra/zebra*

%files bgpd
%defattr(644,root,root,755)
%doc bgpd/*sample*
%{_mandir}/man8/bgpd*
%attr(755,root,root) %{_sbindir}/bgpd
%attr(754,root,root) /etc/rc.d/init.d/bgpd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/bgpd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/bgpd
%ghost /var/log/zebra/bgpd*

%files ospfd
%defattr(644,root,root,755)
%doc ospfd/*sample*
%{_mandir}/man8/ospfd*
%attr(755,root,root) %{_sbindir}/ospfd
%attr(754,root,root) /etc/rc.d/init.d/ospfd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/ospfd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/ospfd
%ghost /var/log/zebra/ospfd*

%files ospf6d
%defattr(644,root,root,755)
%doc ospf6d/*sample*
%{_mandir}/man8/ospf6d*
%attr(755,root,root) %{_sbindir}/ospf6d
%attr(754,root,root) /etc/rc.d/init.d/ospf6d
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/ospf6d
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/ospf6d
%ghost /var/log/zebra/ospf6d*

%files ripd
%defattr(644,root,root,755)
%doc ripd/*sample*
%{_mandir}/man8/ripd*
%attr(755,root,root) %{_sbindir}/ripd
%attr(754,root,root) /etc/rc.d/init.d/ripd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/ripd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/ripd
%ghost /var/log/zebra/ripd*

%files ripngd
%defattr(644,root,root,755)
%doc ripngd/*sample*
%{_mandir}/man8/ripngd*
%attr(755,root,root) %{_sbindir}/ripngd
%attr(754,root,root) /etc/rc.d/init.d/ripngd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/ripngd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/ripngd
%ghost /var/log/zebra/ripngd*
