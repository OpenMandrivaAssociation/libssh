# (tpg) reduce bloat by excluding cmake requires on devel packages
%global __requires_exclude ^cmake.*$

%define major 4
%define libname %mklibname ssh %{major}
%define devname %mklibname ssh -d
%global optflags %{optflags} -Wno-gnu-statement-expression

Summary:	C library to authenticate in a simple manner to one or more SSH servers
Name:		libssh
Epoch:		1
Version:	0.10.6
Release:	1
Group:		System/Libraries
License:	LGPLv2.1+
Url:		http://www.libssh.org
# svn checkout svn://svn.berlios.de/libssh/trunk libssh
Source0:	https://www.libssh.org/files/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Patch1:		libssh-0.10.3-fix-build-where-size_t-is-not-unsigned-long.patch
Patch2:		libssh-fix_conf_checks.patch
BuildRequires:	cmake ninja
BuildRequires:	doxygen
BuildRequires:	pcap-devel
BuildRequires:	krb5-devel
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(openssl) >= 1.1
BuildRequires:	pkgconfig(zlib)

%description
The ssh library was designed to be used by programmers needing a working 
SSH implementation by the mean of a library. The complete control of the 
client is made by the programmer. With libssh, you can remotely execute 
programs, transfer files, use a secure and transparent tunnel for your 
remote programs. With its Secure FTP implementation, you can play with 
remote files easily, without third-party programs others than libcrypto 
(from openssl). libssh features :

    * Full C library functions for manipulating a client-side SSH
      connection
    * Lesser GPL licensing -SSH2 protocol compliant
    * Fully configurable sessions
    * Support for AES-128,AES-192,AES-256,blowfish, in cbc mode
    * Use multiple SSH connections in a same process, at same time
    * Use multiple channels in the same connection
    * Thread safety when using different sessions at same time
    * Basic but correct SFTP implementation (secure file transfer)
    * RSA and DSS server public key supported
    * Compression support (with zlib)
    * Public key (RSA and DSS), password and keyboard-interactive
      authentication
    * Complete documentation about its API
    * Runs and tested under amd64, x86, arm, sparc32, ppc under Linux,
      BSD, MacosX and Solaris
    * A developer listening to you
    * It's free (LGPL)!

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
The ssh library was designed to be used by programmers needing a working
SSH implementation by the mean of a library. The complete control of the
client is made by the programmer. With libssh, you can remotely execute
programs, transfer files, use a secure and transparent tunnel for your
remote programs. With its Secure FTP implementation, you can play with
remote files easily, without third-party programs others than libcrypto
(from openssl).

%files -n %{libname}
%{_libdir}/libssh.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	ssh-devel = %{EVRD}
Provides:	libssh-devel = %{EVRD}

%description -n %{devname}
This package contains the development files for %{name}.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake -DWITH_GCRYPT=ON -DWITH_PCAP=ON -DLIB_INSTALL_DIR=%{_libdir} -G Ninja
%ninja_build

%install
%ninja_install -C build
