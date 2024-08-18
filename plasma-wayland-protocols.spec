Summary:	Plasma Specific Protocols for Wayland
Summary(pl.UTF-8):	Specyficzne dla Plasmy protokoły dla Waylanda
Name:		plasma-wayland-protocols
Version:	1.13.0
Release:	2
License:	LGPL v2.1+, MIT, BSD
Group:		Libraries
Source0:	https://download.kde.org/stable/plasma-wayland-protocols/%{name}-%{version}.tar.xz
# Source0-md5:	5d30de6367ab1ff92b2ece7b159b3c8b
URL:		https://invent.kde.org/libraries/plasma-wayland-protocols.git
BuildRequires:	cmake >= 3.5
BuildRequires:	kf6-extra-cmake-modules >= 5.69.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
Obsoletes:	kf5-plasma-wayland-protocols < 1.13.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
Plasma Specific Protocols for Wayland.

%description -l pl.UTF-8
Specyficzne dla Plasmy protokoły dla Waylanda.

%package devel
Summary:	Development files for Plasma Wayland Protocols
Summary(pl.UTF-8):	Pliki programistyczne protokołów Waylanda dla Plasmy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kf5-plasma-wayland-protocols-devel < 1.13.0

%description devel
This package contains the development files for applications that use
Plasma Wayland Protocols.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki do rozwijania aplikacji wykorzystujących
protokoły Waylanda dla Plasmy.

%prep
%setup -q

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..

%ninja_build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/plasma-wayland-protocols

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/PlasmaWaylandProtocols
