import { Component, OnInit } from '@angular/core';
import { SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent implements OnInit {

  constructor(private service:SharedService) { }

  EscolaList:any=[];
  selectedSchool:any;

  ngOnInit(): void {
    this.refreshDepList();
  }

  refreshDepList() {
    this.selectedSchool = this.service.selectedSchool;
  }
}
