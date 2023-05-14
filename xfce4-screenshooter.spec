Summary:	Screenshooter application and plugin for Xfce panel
Summary(pl.UTF-8):	Aplikacja screenshooter i wtyczka dla panelu Xfce
Name:		xfce4-screenshooter
Version:	1.10.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/apps/xfce4-screenshooter/1.10/%{name}-%{version}.tar.bz2
# Source0-md5:	8d2a6104c1e6ab2347e52b93c1c07f55
Patch0:		desktop-name.patch
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-screenshooter-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	exo-devel >= 0.12.0
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	libsoup3-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	libxfce4ui-devel >= 4.16.0
Requires:	xfce4-dirs >= 4.6
Obsoletes:	xfce4-screenshooter-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application allows you to capture the entire screen, the active
window or a selected region. You can set the delay that elapses before
the screenshot is taken and the action that will be done with the
screenshot: save it to a PNG file, copy it to the clipboard, open it
using another application, or host it on ZimageZ, a free online image
hosting service.

A plugin for the Xfce panel is also available.

%description -l pl.UTF-8
Ta aplikacja umożliwia zrobienie zrzutu ekranu, aktywnego okna albo
zaznaczonego obszaru. Można ustawić opóźnienie przed zrobieniem zrzutu
ekranu i akcję, która zostanie wykonana po: zapisać do pliku PNG,
przenieść do schowka, otworzyć przy pomocy innego programu lub
umieścić na ZimageZ, darmowym serwisie hostowania obrazów.

Dostępna jest też wtyczka dla panelu Xfce.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hye,ie,ur_PK}
# unify
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/xfce4-screenshooter
%{_desktopdir}/xfce4-screenshooter.desktop
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libscreenshooterplugin.so*
%{_datadir}/xfce4/panel/plugins/screenshooter.desktop
%{_iconsdir}/hicolor/*/apps/org.xfce.screenshooter.*
%{_datadir}/metainfo/xfce4-screenshooter.appdata.xml
%{_mandir}/man1/xfce4-screenshooter.1*
