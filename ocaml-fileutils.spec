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


%changelog
* Mon Aug 23 2010 Florent Monnier <blue_prawn@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 572350
- new url (moved permanently)

* Mon Apr 19 2010 Florent Monnier <blue_prawn@mandriva.org> 0.4.0-1mdv2010.1
+ Revision: 536860
- updated to version 0.4.0
- just a retab

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-4mdv2010.1
+ Revision: 496362
- rebuild

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-3mdv2010.0
+ Revision: 389931
- rebuild

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-2mdv2009.1
+ Revision: 318328
- move non-devel files in main package
- site-lib hierarchy doesn't exist anymore

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-1mdv2009.0
+ Revision: 271934
- import ocaml-fileutils


* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-1mdv2009.0
- first mdv release, stolen from redhat
