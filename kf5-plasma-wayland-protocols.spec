%define         kdeframever     5.73
%define         qtver           5.9.0
%define         kfname          plasma-wayland-protocols

Summary:	Plasma Specific Protocols for Wayland
Name:		kf5-%{kfname}
Version:	1.3.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://download.kde.org/stable/%{kfname}/%{kfname}-%{version}.tar.xz
# Source0-md5:	ff5193b515decd1eb8393fed1cfa5bf3
URL:		https://invent.kde.org/libraries/%{kfname}.git
BuildRequires:	kf5-extra-cmake-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
Plasma Specific Protocols for Wayland

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
		-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
		../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/plasma-wayland-protocols/

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/PlasmaWaylandProtocols/
