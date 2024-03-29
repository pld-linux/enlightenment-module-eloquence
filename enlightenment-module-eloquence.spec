#
%define		_module_name	eloquence

Summary:	Enlightenment DR17 module: %{_module_name}
Summary(pl.UTF-8):	Moduł Enlightenmenta DR17: eloquence
Name:		enlightenment-module-%{_module_name}
Version:	0.5.0.1
Release:	1
License:	BSD-like
Group:		X11/Window Managers/Tools
Source0:	http://www.get-e.org/Resources/Modules/_files/%{_module_name}-%{version}.tar.gz
# Source0-md5:	17463227247e05aa2ee15d3963aa34dc
URL:		http://www.get-e.org/Resources/Modules/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bmp-devel
BuildRequires:	edje
BuildRequires:	enlightenment-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRequires:	xmms-devel
Requires:	enlightenment
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment DR17 module: Displays the current playing title using
using XMMS, BMP or Amarok on screen.

%description -l pl.UTF-8
Moduł Enlightenmenta DR17 wyświetlający na ekranie tytuł utworu
aktualnie odtwarzanego przy użyciu XMMS-a, BMP lub Amaroka.

%prep
%setup -q -n %{_module_name}-%{version}
sed -e 's|datadir=.*|datadir="`enlightenment-config --module-dir`/${PACKAGE}"|' \
    -e '/PACKAGE_DATA_DIR/s|"[^"]*"|"`enlightenment-config --module-dir`/${PACKAGE}"|' \
    -e '/PACKAGE_LIB_DIR/s|"[^"]*"|"`enlightenment-config --module-dir`"|' \
    -e 's/$AMAROK/have amarok/' \
    -e '/dlopen/s/^#//' \
    -i configure.in

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL README TODO
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/module.so
# violates FHS
%{_libdir}/enlightenment/modules_extra/%{_module_name}/themes
%{_libdir}/enlightenment/modules_extra/%{_module_name}/module_icon.png
