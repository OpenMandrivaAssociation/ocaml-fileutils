Name:           ocaml-fileutils
Version:        0.4.0
Release:        %mkrel 1
Summary:        OCaml library for common file and filename operations
Group:          Development/Other
License:        LGPLv2 with exceptions
URL:            http://le-gall.net/sylvain+violaine/download/
Source0:        http://le-gall.net/sylvain+violaine/download/ocaml-fileutils-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
./configure --libdir=%{_libdir}

%build
make

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install prefix=%{buildroot}/usr htmldir=%{buildroot}%{_docdir}/%{name}-devel

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
%{_libdir}/ocaml/fileutils/*.cmx
%{_libdir}/ocaml/fileutils/*.ml
%{_libdir}/ocaml/fileutils/*.mli
