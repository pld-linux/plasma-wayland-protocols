%define         kdeframever     5.73
%define         qtver           5.9.0
%define         kfname          plasma-wayland-protocols

Summary:	Plasma Specific Protocols for Wayland
Summary(pl.UTF-8):	Specyficzne dla Plasmy protokoły dla Waylanda
Name:		kf5-%{kfname}
Version:	1.11.1
Release:	1
License:	LGPL v2.1+, MIT, BSD
Group:		Libraries
Source0:	https://download.kde.org/stable/plasma-wayland-protocols/%{kfname}-%{version}.tar.xz
# Source0-md5:	9a62a2c48ec78c19ab8a339bcd8bdddd
URL:		https://invent.kde.org/libraries/plasma-wayland-protocols.git
BuildRequires:	cmake >= 3.5
BuildRequires:	kf5-extra-cmake-modules >= 5.69.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
Plasma Specific Protocols for Wayland.

%description -l pl.UTF-8
Specyficzne dla Plasmy protokoły dla Waylanda.

%package devel
Summary:	Development files for Plasma Wayland Protocols
Summary(pl.UTF-8):	Pliki programistyczne protokołów Waylanda dla Plasmy
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files for applications that use
Plasma Wayland Protocols.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki do rozwijania aplikacji wykorzystujących
protokoły Waylanda dla Plasmy.

%prep
%setup -q -n %{kfname}-%{version}

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
