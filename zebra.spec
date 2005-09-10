#
# Conditional build:
%bcond_with	snmp	# with SNMP support (broken?)
#
Summary:	Routing daemon
Summary(pl):	Demon routingu
Summary(pt_BR):	Servidor de roteamento multi-protocolo
Summary(ru):	äÅÍÏÎ ÍÁÒÛÒÕÔÉÚÁÃÉÉ Zebra
Summary(uk):	äÅÍÏÎ ÍÁÒÛÒÕÔÉÚÁÃ¦§ Zebra
Name:		zebra
Version:	0.94
Release:	2
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.zebra.org/pub/zebra/%{name}-%{version}.tar.gz
# Source0-md5:	ff1633f1ac026b720fa37b1856be3f48
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
BuildRequires:	readline-devel >= 4.1
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	pam-devel
BuildRequires:	texinfo
%{?with_snmp:BuildRequires:	ucd-snmp-devel >= 4.2.6}
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires(post):	/bin/hostname
Provides:	routingdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	bird
Obsoletes:	gated
Obsoletes:	mrt
Obsoletes:	zebra-xs26
Obsoletes:	quagga

%define		_sysconfdir	/etc/%{name}

%description
Zebra is a multi-server routing software package which provides TCP/IP
based routing protocols also with IPv6 support such as RIP, OSPF, BGP
and so on. Zebra turns your machine into a full powered router.

Daemons for each routing protocols are available in separate packages.

%description -l pl
Program do dynamicznego ustawiania tablicy tras. Mo¿e tak¿e ustalaæ
trasy dla IPv6.

Demony obs³uguj±ce poszczególne protoko³y dostêpne s± w osobnych
pakietach.

%description -l pt_BR
Zebra é um servidor múltiplo para roteamento, provendo suporte aos
protocolos baseados em TCP/IP (inclusive IPv6) tais como RIP, OSPF,
BGP, entre outros. Zebra transforma sua máquina em um poderoso
roteador.

%description -l ru
GNU Zebra - ÜÔÏ Ó×ÏÂÏÄÎÏÅ ÐÒÏÇÒÁÍÍÎÏÅ ÏÂÅÓÐÅÞÅÎÉÅ, ÒÁÂÏÔÁÀÝÅÅ Ó
ÏÓÎÏ×ÁÎÎÙÍÉ ÎÁ TCP/IP ÐÒÏÔÏËÏÌÁÍÉ ÍÁÒÛÒÕÔÉÚÁÃÉÉ.

GNU Zebra ÐÏÄÄÅÒÖÉ×ÁÅÔ BGP4, BGP4+, OSPFv2, OSPFv3, RIPv1, RIPv2 É
RIPng.

%description -l uk
GNU Zebra - ÃÅ ×¦ÌØÎÅ ÐÒÏÇÒÁÍÎÅ ÚÁÂÅÚÐÅÞÅÎÎÑ, ÝÏ ÐÒÁÃÀ¤ Ú ÂÁÚÏ×ÁÎÉÍÉ
ÎÁ TCP/IP ÐÒÏÔÏËÏÌÁÍÉ ÍÁÒÛÒÕÔÉÚÁÃ¦§.

GNU Zebra Ð¦ÄÔÒÉÍÕ¤ BGP4, BGP4+, OSPFv2, OSPFv3, RIPv1, RIPv2 ÔÁ
RIPng.

%package bgpd
Summary:	BGP routing daemon
Summary(pl):	Demon routingu BGP
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Obsoletes:	zebra-xs26-bgpd

%description bgpd
BGP routing daemon. Includes IPv6 support.

%description bgpd -l pl
Demon obs³ugi protoko³u BGP. Obs³uguje tak¿e IPv6.

%package ospfd
Summary:	OSPF routing daemon
Summary(pl):	Demon routingu OSPF
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description ospfd
OSPF routing daemon.

%description ospfd -l pl
Demon do obs³ugi protoko³u OSPF.

%package ospf6d
Summary:	IPv6 OSPF routing daemon
Summary(pl):	Demon routingu OSPF w sieciach IPv6
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires(post,preun):	/sbin/chkconfig
Obsoletes:	zebra-xs26-ospf6d

%description ospf6d
OSPF6 routing daemon for IPv6 networks.

%description ospf6d -l pl
Demon obs³ugi protoko³u OSPF w sieciach IPv6.

%package ripd
Summary:	RIP routing daemon
Summary(pl):	Demon routingu RIP
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description ripd
RIP routing daemon for zebra.

%description ripd -l pl
Demon obs³ugi protoko³u RIP.

%package ripngd
Summary:	IPv6 RIP routing daemon
Summary(pl):	Demon routingu RIP w sieciach IPv6
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires(post,preun):	/sbin/chkconfig
Obsoletes:	zebra-xs26-ripngd

%description ripngd
RIP routing daemon for IPv6 networks.

%description ripngd -l pl
Demon obs³ugi protoko³u RIP w sieciach IPv6.

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
	--enable-one-vty \
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
	$RPM_BUILD_ROOT/var/log/{archiv,}/zebra \
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
if [ -f /var/lock/subsys/zebra ]; then
	/etc/rc.d/init.d/zebra restart >&2
else
	echo "Run '/etc/rc.d/init.d/zebra start' to start main routing deamon." >&2
fi

%post bgpd
/sbin/chkconfig --add bgpd >&2
if [ -f /var/lock/subsys/bgpd ]; then
	/etc/rc.d/init.d/bgpd restart >&2
else
	echo "Run '/etc/rc.d/init.d/bgpd start' to start bgpd routing deamon." >&2
fi

%post ospfd
/sbin/chkconfig --add ospfd >&2
if [ -f /var/lock/subsys/ospfd ]; then
	/etc/rc.d/init.d/ospfd restart >&2
else
	echo "Run '/etc/rc.d/init.d/ospfd start' to start ospfd routing deamon." >&2
fi

%post ospf6d
/sbin/chkconfig --add ospf6d >&2
if [ -f /var/lock/subsys/ospf6d ]; then
	/etc/rc.d/init.d/ospf6d restart >&2
else
	echo "Run '/etc/rc.d/init.d/ospf6d start' to start ospf6d routing deamon." >&2
fi

%post ripd
/sbin/chkconfig --add ripd >&2
if [ -f /var/lock/subsys/ripd ]; then
	/etc/rc.d/init.d/ripd restart >&2
else
	echo "Run '/etc/rc.d/init.d/ripd start' to start ripd routing deamon." >&2
fi

%post ripngd
/sbin/chkconfig --add ripngd >&2
if [ -f /var/lock/subsys/ripngd ]; then
	/etc/rc.d/init.d/ripngd restart >&2
else
	echo "Run '/etc/rc.d/init.d/ripngd start' to start ripngd routing deamon." >&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/zebra ]; then
		/etc/rc.d/init.d/zebra stop >&2
	fi
	/sbin/chkconfig --del zebra >&2
fi

%preun bgpd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/bgpd ]; then
		/etc/rc.d/init.d/bgpd stop >&2
	fi
	/sbin/chkconfig --del bgpd >&2
fi

%preun ospfd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/ospfd ]; then
		/etc/rc.d/init.d/ospfd stop >&2
	fi
	/sbin/chkconfig --del ospfd >&2
fi

%preun ospf6d
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/ospf6d ]; then
		/etc/rc.d/init.d/ospf6d stop >&2
	fi
	/sbin/chkconfig --del ospf6d >&2
fi

%preun ripd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/ripd ]; then
		/etc/rc.d/init.d/ripd stop >&2
	fi
	/sbin/chkconfig --del ripd >&2
fi

%preun ripngd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/ripngd ]; then
		/etc/rc.d/init.d/ripngd stop >&2
	fi
	/sbin/chkconfig --del ripngd >&2
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README REPORTING-BUGS SERVICES TODO
%{_infodir}/*info*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
%dir %attr(750,root,root) %{_sysconfdir}
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) %{_sysconfdir}/*.conf
%config(noreplace) %verify(not md5 size mtime) /etc/pam.d/zebra
%dir %attr(750,root,root) /var/run/zebra
%dir %attr(750,root,root) /var/log/zebra
%dir %attr(750,root,root) /var/log/archiv/zebra

%doc zebra/*sample*
%{_mandir}/man8/zebra*
%attr(755,root,root) %{_sbindir}/zebra
%attr(754,root,root) /etc/rc.d/init.d/zebra
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/sysconfig/zebra
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/logrotate.d/zebra
%ghost /var/log/zebra/zebra*

%files bgpd
%defattr(644,root,root,755)
%doc bgpd/*sample*
%{_mandir}/man8/bgpd*
%attr(755,root,root) %{_sbindir}/bgpd
%attr(754,root,root) /etc/rc.d/init.d/bgpd
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/sysconfig/bgpd
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/logrotate.d/bgpd
%ghost /var/log/zebra/bgpd*

%files ospfd
%defattr(644,root,root,755)
%doc ospfd/*sample*
%{_mandir}/man8/ospfd*
%attr(755,root,root) %{_sbindir}/ospfd
%attr(754,root,root) /etc/rc.d/init.d/ospfd
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/sysconfig/ospfd
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/logrotate.d/ospfd
%ghost /var/log/zebra/ospfd*

%files ospf6d
%defattr(644,root,root,755)
%doc ospf6d/*sample*
%{_mandir}/man8/ospf6d*
%attr(755,root,root) %{_sbindir}/ospf6d
%attr(754,root,root) /etc/rc.d/init.d/ospf6d
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/sysconfig/ospf6d
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/logrotate.d/ospf6d
%ghost /var/log/zebra/ospf6d*

%files ripd
%defattr(644,root,root,755)
%doc ripd/*sample*
%{_mandir}/man8/ripd*
%attr(755,root,root) %{_sbindir}/ripd
%attr(754,root,root) /etc/rc.d/init.d/ripd
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/sysconfig/ripd
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/logrotate.d/ripd
%ghost /var/log/zebra/ripd*

%files ripngd
%defattr(644,root,root,755)
%doc ripngd/*sample*
%{_mandir}/man8/ripngd*
%attr(755,root,root) %{_sbindir}/ripngd
%attr(754,root,root) /etc/rc.d/init.d/ripngd
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/sysconfig/ripngd
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/logrotate.d/ripngd
%ghost /var/log/zebra/ripngd*
