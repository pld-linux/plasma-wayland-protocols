%define         kdeframever     5.73
%define         qtver           5.9.0
%define         kfname          plasma-wayland-protocols

Name:		kf5-%{kfname}
Group:		Library
Version:	1.1.1
Release:	0.1
Summary:	Plasma Specific Protocols for Wayland

License:	GPLv2+
URL:		https://invent.kde.org/libraries/%{kfname}.git
Source0:	https://download.kde.org/stable/%{kfname}/%{version}/%{kfname}-%{version}.tar.xz
# Source0-md5:	82207f4df5e4a91452339bcf7b983d7e

BuildRequires:	kf5-extra-cmake-modules
#BuildRequires:	qt5-qtbase-devel

%description
Plasma Specific Protocols for Wayland

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description	devel
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

%files
%defattr(644,root,root,755)
%{_datadir}/plasma-wayland-protocols/

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/PlasmaWaylandProtocols/

