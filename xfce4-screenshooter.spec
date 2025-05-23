Summary:	Screenshooter application and plugin for Xfce panel
Summary(pl.UTF-8):	Aplikacja screenshooter i wtyczka dla panelu Xfce
Name:		xfce4-screenshooter
Version:	1.11.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/apps/xfce4-screenshooter/1.11/%{name}-%{version}.tar.xz
# Source0-md5:	c1ac25c948a949c699c2034f7d3af56d
Patch0:		desktop-name.patch
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-screenshooter-plugin
BuildRequires:	exo-devel >= 0.12.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.66.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	libxfce4ui-devel >= 4.18.0
BuildRequires:	libxfce4util-devel >= 4.18.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	wayland-devel >= 1.20.0
BuildRequires:	wayland-protocols >= 1.25
BuildRequires:	xfce4-dev-tools >= 4.18.0
BuildRequires:	xfce4-panel-devel >= 4.18.0
BuildRequires:	xorg-lib-libX11-devel >= 1.6.7
BuildRequires:	xorg-lib-libXext-devel >= 1.0.0
BuildRequires:	xorg-lib-libXfixes-devel >= 4.0.0
BuildRequires:	xorg-lib-libXi-devel >= 1.7.8
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
%patch -P 0 -p1

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
