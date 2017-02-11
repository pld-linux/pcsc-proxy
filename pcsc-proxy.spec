#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	PC/SC Proxy for Linux
Summary(de.UTF-8):	PC/SC Proxy für Linux
Summary(pl.UTF-8):	Proxy PC/SC dla Linuksa
Name:		pcsc-proxy
Version:	2.0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
# https://www.aquamaniac.de/sites/download/packages.php
Source0:	https://www.aquamaniac.de/sites/download/download.php?package=11&release=05&file=01&dummy=/%{name}-%{version}.tar.gz
# Source0-md5:	229b3c3e42af75960bc680e3f179803e
URL:		https://www.aquamaniac.de/sites/home/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	gnutls-devel
BuildRequires:	libtool
BuildRequires:	pcsc-lite-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PC/SC Proxy for Linux.

%description -l de.UTF-8
PC/SC Proxy für Linux.

%description -l pl.UTF-8
Proxy PC/SC dla Linuksa.

%package client
Summary:	PC/SC Proxy for Linux - client library
Summary(de.UTF-8):	PC/SC Proxy für Linux - Client
Summary(pl.UTF-8):	Proxy PC/SC dla Linuksa - biblioteka kliencka
Group:		Libraries

%description client
PC/SC Proxy for Linux - client library.

%description client -l de.UTF-8
PC/SC Proxy für Linux - Client.

%description client -l pl.UTF-8
Proxy PC/SC dla Linuksa - biblioteka kliencka.

%package server
Summary:	PC/SC Proxy for Linux - server
Summary(de.UTF-8):	PC/SC Proxy für Linux - Server
Summary(pl.UTF-8):	Proxy PC/SC dla Linuksa - serwer
Group:		Daemons

%description server
PC/SC Proxy for Linux - server.

%description server -l de.UTF-8
PC/SC Proxy für Linux - Server.

%description server -l pl.UTF-8
Proxy PC/SC dla Linuksa - serwer.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not for development
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpcsclite.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	client -p /sbin/ldconfig
%postun	client -p /sbin/ldconfig

%files client
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libpcsclite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcsclite.so.1

%files server
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_sbindir}/pcsc-proxy
