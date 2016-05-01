%define major 4
%define libname %mklibname ssh %{major}
%define libthreads %mklibname ssh_threads %{major}
%define devname %mklibname ssh -d

Summary:	C library to authenticate in a simple manner to one or more SSH servers
Name:		libssh
Epoch:		1
Version:	0.7.3
Release:	2
Group:		System/Libraries
License:	LGPLv2.1+
Url:		http://www.libssh.org
# svn checkout svn://svn.berlios.de/libssh/trunk libssh
Source0:	https://red.libssh.org/attachments/download/41/%{name}-%{version}.tar.xz
Patch0:		libssh-0.6.3-clang.patch
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	pcap-devel
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(openssl)
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

%package -n %{libthreads}
Summary:	Main library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}ssh4 < 0.5.4-2

%description -n %{libthreads}
This package contains a shared library for %{name}.

%files -n %{libthreads}
%{_libdir}/libssh_threads.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	%{libthreads} = %{EVRD}
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
%setup -q
%apply_patches

%build
%cmake -DWITH_GCRYPT=ON -DWITH_PCAP=ON
%make

%install
%makeinstall_std -C build

