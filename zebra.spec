#
# _without_snmp - without SNMP support (problematic with IPv6?)
Summary:	Routing daemon
Summary(pl):	Demon routingu
Name:		zebra
Version:	0.92a
Release:	2
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.zebra.org/pub/zebra/%{name}-%{version}.tar.gz
Source1:	%{name}-%{name}.init
Source2:	%{name}-bgpd.init
Source3:	%{name}-ospf6d.init
Source4:	%{name}-ospfd.init
Source5:	%{name}-ripd.init
Source6:	%{name}-ripngd.init
Source7:	%{name}.sysconfig
Source8:	%{name}.logrotate
Source9:	%{name}.pam
Patch1:		%{name}-proc.patch
Patch2:		%{name}-socket_paths.patch
Patch3:		%{name}-autoconf.patch
Patch4:		%{name}-automake.patch
Patch5:		%{name}-autoheader.patch
URL:		http://www.zebra.org/
BuildRequires:	texinfo
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.1
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	pam-devel
%{?!_without_snmp:BuildRequires:	ucd-snmp-devel >= 4.2.3}
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
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
Program do dynamicznego ustawiania tablicy tras. Mo¿e tak¿e ustalaæ
trasy dla IPv6.

%prep
%setup  -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f ./missing
rm -f doc/zebra.info
aclocal
autoconf
automake -a -c
autoheader
%configure \
	--enable-one-vty \
	--enable-ipv6 \
	--enable-netlink \
	%{?_without_snmp:--disable-snmp} \
	%{?!_without_snmp:--enable-snmp} \
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

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/zebra
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/bgpd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/ospf6d
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/ospfd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/ripd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/ripngd
install %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/zebra
install %{SOURCE8} $RPM_BUILD_ROOT/etc/logrotate.d/zebra
install %{SOURCE9} $RPM_BUILD_ROOT/etc/pam.d/zebra

touch $RPM_BUILD_ROOT/var/log/zebra/{zebra,bgpd,ospf6d,ospfd,ripd,ripngd}.log

gzip -9nf AUTHORS NEWS README REPORTING-BUGS SERVICES TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

/sbin/chkconfig --add zebra >&2
/sbin/chkconfig --add bgpd >&2
/sbin/chkconfig --add ospf6d >&2
/sbin/chkconfig --add ospfd >&2
/sbin/chkconfig --add ripd >&2
/sbin/chkconfig --add ripngd >&2

touch $RPM_BUILD_ROOT/var/log/zebra/{zebra,bgpd,ospf6d,ospfd,ripd,ripngd}.log

if [ ! -e %{_sysconfdir}/zebra.conf ]; then
        echo "hostname `hostname`" > %{_sysconfdir}/zebra.conf
        chmod 640 %{_sysconfdir}/zebra.conf
fi
if [ ! -e %{_sysconfdir}/vtysh.conf ]; then
        touch %{_sysconfdir}/vtysh.conf
        chmod 640 %{_sysconfdir}/vtysh.conf
fi

if [ -f /var/lock/subsys/zebra ]; then
	/etc/rc.d/init.d/zebra restart >&2
else
	echo "Run '/etc/rc.d/init.d/zebra start' to start main routing deamon." >&2
fi

if [ -f /var/lock/subsys/bgpd ]; then
	/etc/rc.d/init.d/bgpd restart >&2
else
	echo "Run '/etc/rc.d/init.d/bgpd start' to start bgpd routing deamon." >&2
fi

if [ -f /var/lock/subsys/ospf6d ]; then
	/etc/rc.d/init.d/ospf6d restart >&2
else
	echo "Run '/etc/rc.d/init.d/ospf6d start' to start ospf6d routing deamon." >&2
fi

if [ -f /var/lock/subsys/ospfd ]; then
	/etc/rc.d/init.d/ospfd restart >&2
else
	echo "Run '/etc/rc.d/init.d/ospfd start' to start ospfd routing deamon." >&2
fi

if [ -f /var/lock/subsys/ripd ]; then
	/etc/rc.d/init.d/ripd restart >&2
else
	echo "Run '/etc/rc.d/init.d/ripd start' to start ripd routing deamon." >&2
fi

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

	if [ -f /var/lock/subsys/bgpd ]; then
		/etc/rc.d/init.d/bgpd stop >&2
	fi
        /sbin/chkconfig --del bgpd >&2

	if [ -f /var/lock/subsys/ospf6d ]; then
		/etc/rc.d/init.d/ospf6d stop >&2
	fi
        /sbin/chkconfig --del ospf6d >&2

	if [ -f /var/lock/subsys/ospfd ]; then
		/etc/rc.d/init.d/ospfd stop >&2
	fi
        /sbin/chkconfig --del ospfd >&2

	if [ -f /var/lock/subsys/ripd ]; then
		/etc/rc.d/init.d/ripd stop >&2
	fi
        /sbin/chkconfig --del ripd >&2

	if [ -f /var/lock/subsys/ripngd ]; then
		/etc/rc.d/init.d/ripngd stop >&2
	fi
        /sbin/chkconfig --del ripngd >&2
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc */*sample* *.gz
%{_infodir}/*info*
%{_mandir}/man?/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%attr(754,root,root) /etc/rc.d/init.d/*
%config(noreplace) %verify(not md5 size mtime) /etc/pam.d/zebra
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/sysconfig/*
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) /etc/logrotate.d/*
%dir %attr(750,root,root) %{_sysconfdir}
%dir %attr(750,root,root) /var/run/zebra
%dir %attr(750,root,root) /var/log/zebra
%dir %attr(750,root,root) /var/log/archiv/zebra
%ghost /var/log/zebra/*
