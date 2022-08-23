#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : freeglut
Version  : 3.2.2
Release  : 23
URL      : https://sourceforge.net/projects/freeglut/files/freeglut/3.2.2/freeglut-3.2.2.tar.gz
Source0  : https://sourceforge.net/projects/freeglut/files/freeglut/3.2.2/freeglut-3.2.2.tar.gz
Summary  : A freely licensed and improved alternative to the GLUT library
Group    : Development/Tools
License  : MIT
Requires: freeglut-lib = %{version}-%{release}
Requires: freeglut-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glu-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : mesa-dev

%description
BRIEF OVERVIEW
==============
This is the freeglut package.
Freeglut, the Free OpenGL Utility Toolkit, is meant to be a free alternative to
Mark Kilgard's GLUT library. Freeglut is free software, distributed under an
MIT/X11 style license. You are free to use, modify, and redistribute FreeGLUT
with or without modifications (see COPYING for details).

%package dev
Summary: dev components for the freeglut package.
Group: Development
Requires: freeglut-lib = %{version}-%{release}
Provides: freeglut-devel = %{version}-%{release}
Requires: freeglut = %{version}-%{release}

%description dev
dev components for the freeglut package.


%package lib
Summary: lib components for the freeglut package.
Group: Libraries
Requires: freeglut-license = %{version}-%{release}

%description lib
lib components for the freeglut package.


%package license
Summary: license components for the freeglut package.
Group: Default

%description license
license components for the freeglut package.


%prep
%setup -q -n freeglut-3.2.2
cd %{_builddir}/freeglut-3.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656110852
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1656110852
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/freeglut
cp %{_builddir}/freeglut-3.2.2/COPYING %{buildroot}/usr/share/package-licenses/freeglut/952348c4126a5946c98385d2fe5a4801735f174d
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/GL/freeglut.h
/usr/include/GL/freeglut_ext.h
/usr/include/GL/freeglut_std.h
/usr/include/GL/freeglut_ucall.h
/usr/include/GL/glut.h
/usr/lib64/cmake/FreeGLUT/FreeGLUTConfig.cmake
/usr/lib64/cmake/FreeGLUT/FreeGLUTConfigVersion.cmake
/usr/lib64/cmake/FreeGLUT/FreeGLUTTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeGLUT/FreeGLUTTargets.cmake
/usr/lib64/libglut.so
/usr/lib64/pkgconfig/glut.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libglut.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libglut.so.3
/usr/lib64/glibc-hwcaps/x86-64-v3/libglut.so.3.11.1
/usr/lib64/libglut.so.3
/usr/lib64/libglut.so.3.11.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/freeglut/952348c4126a5946c98385d2fe5a4801735f174d
