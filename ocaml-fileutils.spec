%define name	ocaml-fileutils
%define version	0.3.0
%define release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    OCaml library for common file and filename operations
Group:      Development/Other
License:    LGPLv2 with exceptions
URL:        http://www.gallu.homelinux.org/download/
Source0:    http://www.gallu.homelinux.org/download/ocaml-fileutils-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This library is intended to provide a basic interface to the most
common file and filename operations.  It provides several different
filename functions: reduce, make_absolute, make_relative...  It also
enables you to manipulate real files: cp, mv, rm, touch...

It is separated into two modules: SysUtil and SysPath.  The first one
manipulates real files, the second one is made for manipulating
abstract filenames.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q
# The whole build system for this package is totally broken.
# We build into a temporary directory then copy the files
# to the right place.
./configure --prefix=%{_prefix} --libdir=%{_libdir} \
  --enable-ocamlfind \
  --with-builddir=`pwd`/tmp

%build
# Nothing: 'make' builds and installs.  Stupid!

%install
# Go and do your broken stuff now ...
rm -rf tmp
make
# make doc   (borked)

# ... and copy the files to the right places.
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
cp -r tmp/lib/fileutils %{buildroot}%{_libdir}/ocaml
rm -rf tmp

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc COPYING
%dir %{_libdir}/ocaml/fileutils
%{_libdir}/ocaml/fileutils/*.cmi
%{_libdir}/ocaml/fileutils/*.cma
%{_libdir}/ocaml/fileutils/META

%files devel
%defattr(-,root,root)
%doc COPYING AUTHOR CHANGELOG README TODO
%{_libdir}/ocaml/fileutils/*.a
%{_libdir}/ocaml/fileutils/*.cmxa

