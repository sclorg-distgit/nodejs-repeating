%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global npm_name repeating

Summary:       Repeat a string - fast
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.0.0
Release:       8%{?dist}
License:       MIT
URL:           https://github.com/sindresorhus/repeating
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Repeat a string - fast

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc license readme.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Mar 08 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-8
- Add symlink macro

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-7
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-6
- Rebuilt with updated metapackage

* Fri Jan 15 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-5
- Enable find_provides_and_requires macro

* Wed Jan 06 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-3
- Enable scl macros

* Thu Sep 10 2015 Troy Dawson <tdawson@redhat.com>
- spec change: npmname -> npm_name

* Thu Sep 10 2015 Troy Dawson <tdawson@redhat.com> - 2.0.0-1
- Initial package
